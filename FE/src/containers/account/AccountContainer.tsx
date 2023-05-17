/* eslint-disable react-hooks/exhaustive-deps */
"use client";
import {
  AcountContainer,
  AcountCard,
  AcountDisabledFiled,
} from "@/components/account/styles";
import {
  Box,
  Button,
  FormControl,
  Input,
  InputLabel,
  MenuItem,
  Select,
  SelectChangeEvent,
  Stack,
  TextField,
  Typography,
} from "@mui/material";
import { blue, grey } from "@mui/material/colors";
import Countries from "@/data/countries.json";
import uuid from "react-uuid";
import { InCountry } from "@/service/auth_service";
import { useEffect, useState } from "react";
import { useAuth } from "@/contexts/auth.context";
import { redirect } from "next/navigation";
import AccountListTitle from "@/components/account/AccountListTitle";
import AccountList, {
  AccountListHead,
  AccountListRow,
  AccountTd,
} from "@/components/account/AccountList";
import AccountNoList from "@/components/account/AccountNoList";
import AccountDialog from "@/components/account/AccountDialog";
import {
  changeCorUserInfo,
  changeUserInfo,
  deleteCorUser,
  deleteUser,
} from "@/service/account_service";
import { useSnackbar } from "notistack";

const subs = [
  {
    Category: "dd1",
    Company: "Samsung",
    StartAt: "2023.00.00",
    EndAt: "2023.00.00",
  },
  {
    Category: "dd2",
    Company: "LG",
    StartAt: "2023.00.00",
    EndAt: "2023.00.00",
  },
  {
    Category: "dd1",
    Company: "SK",
    StartAt: "2023.00.00",
    EndAt: "2023.00.00",
  },
];
const SUB_COL = ["Category", "Company", "Start At", "End At"];

interface DataProps {
  data: {
    name: string;
    password: string;
    email: string;
    country: string;
    phone: string;
    corporate_name?: string;
    business_num?: string;
  };
}
interface Props extends DataProps {
  id: string;
}

export default function AccountContainer({ id, data }: Props) {
  const { user, signOut } = useAuth();
  const { enqueueSnackbar } = useSnackbar();

  if (!user || decodeURI(decodeURIComponent(id)) !== user?.email) {
    redirect("/");
  }

  const [name, setName] = useState<string>(data.name);
  const [pw, setPw] = useState<string>(data.password);
  const [country, setCountry] = useState<string>(data.country);

  const phoneArr = data.phone ? data.phone.split(")") : "";
  const [diCode, setDiCode] = useState<string>(
    Array.isArray(phoneArr) ? phoneArr[0] : ""
  );
  const [phoneNum, setPhoneNum] = useState<string>(
    Array.isArray(phoneArr) ? phoneArr[1] : ""
  );

  const isCorCheck = data.corporate_name && data.business_num ? true : false;
  const [isCor, setIsCor] = useState<boolean>(isCorCheck);
  const [corName, setCorName] = useState<string>(
    data.corporate_name ? data.corporate_name : ""
  );
  const [bsNum, setBsNum] = useState<string>(
    data.business_num ? data.business_num : ""
  );

  const handleSelect = (event: SelectChangeEvent) => {
    setCountry(event.target.value);
  };
  useEffect(() => {
    if (country) {
      const findDiCountry = Countries.filter((el) => el.name === country);
      if (findDiCountry.length > 0) {
        setDiCode(
          findDiCountry[0].dial_code ? findDiCountry[0].dial_code : "unknown"
        );
      }
    } else {
      setDiCode("");
    }
  }, [country]);

  const handleChangeAcount = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    if (name === "name") setName(value);
    if (name === "pw") setPw(value);
    if (name === "phone_num") {
      const regex = /^[0-9\b -]{0,13}$/;
      if (regex.test(e.target.value)) {
        setPhoneNum(value);
      }
    }
    if (name === "corName") setCorName(value);
    if (name === "bsNum") setBsNum(value);
  };
  useEffect(() => {
    if (phoneNum.length === 10) {
      setPhoneNum(phoneNum.replace(/(\d{2})(\d{4})(\d{4})/, "$1-$2-$3"));
    }
    if (phoneNum.length === 13) {
      setPhoneNum(
        phoneNum.replace(/-/g, "").replace(/(\d{3})(\d{4})(\d{4})/, "$1-$2-$3")
      );
    }
  }, [phoneNum]);

  const [open, setOpen] = useState<boolean>(false);
  const [title, setTitle] = useState<string>("");
  const [message, setMessage] = useState<string>("");
  const [isModify, setIsModify] = useState<boolean>(true);

  const handleCloseModal = () => {
    setOpen(false);
  };

  const handleOpenModify = () => {
    setOpen(true);
    setTitle("Do you want to save the changes?");
    setMessage("");
    setIsModify(true);
  };
  const handleOpenDelete = () => {
    setOpen(true);
    setTitle("Are you sure you want to withdraw your membership?");
    setMessage("You can't sign up again with the withdrawn email account");
    setIsModify(false);
  };

  const handleModifyUser = async () => {
    try {
      if (!name || !pw || !country || !phoneNum)
        return enqueueSnackbar("Enter all field", { variant: "warning" });
      // 일반 전화번호 표현식
      const regPhone = /^\d{2,3}-?\d{3,4}-?\d{4}$/;
      if (!regPhone.test(phoneNum)) {
        return enqueueSnackbar("Doesn't fit the phone number form", {
          variant: "warning",
        });
      }
      const result = await changeUserInfo({
        name,
        password: pw,
        email: user.email,
        country,
        phone: `${diCode})${phoneNum}`,
        auth_state: "정상",
      });
      if (result.message === "변경되었습니다.") {
        enqueueSnackbar("Change successful", { variant: "success" });
        setOpen(false);
        window.location.reload();
      }
    } catch (err) {
      console.error(err);
      enqueueSnackbar("Server Error", { variant: "error" });
    }
  };
  const handleModifyCorUser = async () => {
    try {
      if (!name || !pw || !country || !phoneNum || !corName || !bsNum)
        return enqueueSnackbar("Enter all field", { variant: "warning" });
      // 일반 전화번호 표현식
      const regPhone = /^\d{2,3}-?\d{3,4}-?\d{4}$/;
      if (!regPhone.test(phoneNum)) {
        return enqueueSnackbar("Doesn't fit the phone number form", {
          variant: "warning",
        });
      }
      const result = await changeCorUserInfo({
        name,
        password: pw,
        email: user.email,
        country,
        phone: `${diCode})${phoneNum}`,
        corporate_name: corName,
        business_num: bsNum,
        auth_state: "정상",
      });
      if (result.message === "변경되었습니다.") {
        enqueueSnackbar("Change successful", { variant: "success" });
        setOpen(false);
        window.location.reload();
      }
    } catch (err) {
      console.error(err);
      enqueueSnackbar("Server Error", { variant: "error" });
    }
  };

  const handleDeleteUser = async () => {
    try {
      if (!user) return;
      const result = await deleteUser({ email: user.email });
      if (result.message === "변경되었습니다.") {
        enqueueSnackbar("Deactivated successful", { variant: "success" });
        setOpen(false);
        signOut();
      }
    } catch (err) {
      console.error(err);
      enqueueSnackbar("Server Error", { variant: "error" });
    }
  };

  const handleDeleteCorUser = async () => {
    try {
      if (!user) return;
      const result = await deleteCorUser({ email: user.email });
      if (result.message === "변경되었습니다.") {
        enqueueSnackbar("Deactivated successful", { variant: "success" });
        setOpen(false);
        signOut();
      }
    } catch (err) {
      console.error(err);
      enqueueSnackbar("Server Error", { variant: "error" });
    }
  };

  return (
    <>
      <AcountContainer>
        <AcountCard maxWidth={590}>
          <Stack direction={"column"}>
            <Typography
              variant="h2"
              fontSize={18}
              fontWeight={"bold"}
              mb={5}
              display={"flex"}
              alignItems={"flex-end"}
            >
              MYPAGE
              <Typography fontSize={12} color={blue[500]} ml={1}>
                {isCor ? `(Corporate)` : `(Individual)`}
              </Typography>
            </Typography>
            <Stack direction={"column"} gap={2} mb={5}>
              <TextField
                label="Name"
                type="text"
                autoComplete="userName"
                variant="standard"
                name="name"
                value={name ? name : ""}
                onChange={handleChangeAcount}
              />
              <AcountDisabledFiled
                label="Email"
                type="text"
                autoComplete="userEmail"
                variant="standard"
                name="email"
                value={user?.email}
                disabled
              />
              <TextField
                label="Password"
                type="password"
                autoComplete="new-password"
                variant="standard"
                name="pw"
                value={pw ? pw : ""}
                onChange={handleChangeAcount}
              />
              <FormControl variant="standard">
                <InputLabel id="demo-simple-select-standard-label">
                  Select Country
                </InputLabel>
                <Select value={country} onChange={handleSelect} label="country">
                  <MenuItem value="">
                    <em>Select Country</em>
                  </MenuItem>
                  {Countries?.map((el: InCountry) => (
                    <MenuItem key={uuid()} value={el.name}>
                      {el.name}
                    </MenuItem>
                  ))}
                </Select>
              </FormControl>
              <Stack direction={"row"} alignItems={"flex-end"}>
                <FormControl variant="standard" sx={{ width: 80 }}>
                  <InputLabel htmlFor="dicode">Dial</InputLabel>
                  <Input id="dicode" value={diCode ? diCode : ""} readOnly />
                </FormControl>
                <FormControl variant="standard" sx={{ flex: 1 }}>
                  <InputLabel htmlFor="userPhone">Phone</InputLabel>
                  <Input
                    id="userPhone"
                    type={"text"}
                    value={phoneNum ? phoneNum : ""}
                    name="phone_num"
                    onChange={handleChangeAcount}
                  />
                </FormControl>
              </Stack>
              {isCor && (
                <>
                  <TextField
                    label="Corporate Name"
                    type="text"
                    autoComplete="CorporateName"
                    variant="standard"
                    name="corName"
                    value={corName ? corName : ""}
                    onChange={handleChangeAcount}
                  />
                  <TextField
                    label="Business Number"
                    type="text"
                    autoComplete="BusinessNumber"
                    variant="standard"
                    name="bsNum"
                    value={bsNum ? bsNum : ""}
                    onChange={handleChangeAcount}
                  />
                </>
              )}
            </Stack>
            <AccountListTitle title={"Subscription history"} goto={"/"} />
            <AccountList>
              <AccountListHead>
                {SUB_COL.map((el) => (
                  <AccountTd key={uuid()}>{el}</AccountTd>
                ))}
              </AccountListHead>
              {subs.map((el) => (
                <AccountListRow key={uuid()}>
                  <AccountTd>{el.Category}</AccountTd>
                  <AccountTd>{el.Company}</AccountTd>
                  <AccountTd>{el.StartAt}</AccountTd>
                  <AccountTd>{el.EndAt}</AccountTd>
                </AccountListRow>
              ))}
            </AccountList>
            <AccountListTitle title={"Payment history"} goto={"/"} />
            <AccountList>
              <AccountNoList message={"No Payment history"} />
            </AccountList>
            <Stack direction={"column"} alignItems={"center"} mb={4}>
              <Box width={1} maxWidth={300}>
                <Typography fontSize={10} color={grey[400]} mb={0.5}>
                  To save changes
                </Typography>
                <Button
                  onClick={handleOpenModify}
                  variant="contained"
                  fullWidth
                  sx={{ height: 40 }}
                >
                  CHANGE
                </Button>
              </Box>
            </Stack>
            <Stack
              direction={"row"}
              justifyContent={"center"}
              alignItems={"center"}
            >
              <Typography fontSize={10} color={grey[400]} mr={0.5}>
                If you no longer use Sentinel Korea KYC?
              </Typography>
              <Button
                onClick={handleOpenDelete}
                sx={{
                  fontSize: 10,
                  color: "#5B7FFF",
                  textDecoration: "underline",
                }}
              >
                Withdrawal
              </Button>
            </Stack>
          </Stack>
        </AcountCard>
      </AcountContainer>
      <AccountDialog
        title={title}
        message={message}
        open={open}
        close={handleCloseModal}
        onClick={
          !isModify && isCor
            ? handleDeleteCorUser
            : !isModify && !isCor
            ? handleDeleteUser
            : isModify && isCor
            ? handleModifyCorUser
            : handleModifyUser
        }
      />
    </>
  );
}
