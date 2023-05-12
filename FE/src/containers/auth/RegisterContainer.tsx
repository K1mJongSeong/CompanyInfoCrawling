"use client";

import {
  AuthContainer,
  AuthCard,
  RegisterTabs,
  RegisterTab,
  AuthCheckBox,
} from "@/components/auth/styled";
import {
  CoUserRegister,
  InCountry,
  UserRegister,
  VerifyCode,
} from "@/service/auth_service";
import VerifyAuth from "@/utils/auth/verified";
import {
  Box,
  Button,
  FormControl,
  Input,
  InputAdornment,
  InputLabel,
  Link,
  MenuItem,
  Select,
  SelectChangeEvent,
  Stack,
  TextField,
  Typography,
} from "@mui/material";
import { grey } from "@mui/material/colors";
import { useSnackbar } from "notistack";
import { useState } from "react";
import { AiFillCheckCircle, AiOutlineCheckCircle } from "react-icons/ai";
import Countries from "@/data/countries.json";
import uuid from "react-uuid";
import TabPanel from "@/components/auth/items/TabPanel";
import { useRouter } from "next/navigation";

function a11yProps(index: number) {
  return {
    id: `simple-tab-${index}`,
    "aria-controls": `simple-tabpanel-${index}`,
  };
}

const Checklabel = {
  inputProps: { "aria-label": "Term Checkbox", name: "agree" },
};

export default function RegisterContainer() {
  const router = useRouter();
  const [tabValue, setTabValue] = useState<number>(0);
  const handleChangeJoinType = (
    event: React.SyntheticEvent,
    newValue: number
  ) => {
    setTabValue(newValue);
    initialRegisterForm();
  };

  const { enqueueSnackbar } = useSnackbar();

  const { verifyEmail } = new VerifyAuth();

  //** field */
  const [name, setName] = useState<string>("");
  const [corName, setCorName] = useState<string>("");
  const [bsNum, setbsNum] = useState<string>("");
  const [country, setCountry] = useState<string>("");

  const [email, setEmail] = useState<string>("");
  const [code, setCode] = useState<string>("");

  const [pw, setPw] = useState<string>("");
  const [pwConfirm, setPwConfirm] = useState<string>("");

  const [agree, setAgree] = useState<boolean>(false);

  //** status */
  const [sended, setSended] = useState<boolean>(false);
  const [verified, setVerified] = useState<boolean>(false);

  const handleChangeRegisterField = (
    e: React.ChangeEvent<HTMLInputElement>
  ) => {
    const { name, value } = e.target;
    if (name === "name") setName(value);
    if (name === "corName") setCorName(value);
    if (name === "bsNum") setbsNum(value);
    if (name === "email") setEmail(value);
    if (name === "code") setCode(value);
    if (name === "pw") setPw(value);
    if (name === "pwConfirm") setPwConfirm(value);
  };

  const handleSelect = (event: SelectChangeEvent) => {
    setCountry(event.target.value);
  };

  const handleClicSendEmail = async () => {
    const result = await verifyEmail(email, enqueueSnackbar);
    if (result === true) {
      setSended(true);
    }
  };

  const handleClickVerified = async () => {
    try {
      if (!code) {
        enqueueSnackbar("Enter Code", { variant: "warning" });
        return false;
      }
      const result = await VerifyCode({ email, code });
      if (result.message === "인증되었습니다.") {
        enqueueSnackbar("Verified Code", { variant: "success" });
        setVerified(true);
      } else {
        enqueueSnackbar("Checkout Code", { variant: "warning" });
        return false;
      }
    } catch (err) {
      enqueueSnackbar("Server Error", { variant: "error" });
      return false;
    }
  };

  const handleRegister = async () => {
    try {
      let result;
      if (!name || !email || !country || !pw || !pwConfirm) {
        enqueueSnackbar("Please enter all the information", {
          variant: "warning",
        });
        return false;
      }
      if (!verified) {
        enqueueSnackbar("Please verify your email", {
          variant: "warning",
        });
        return false;
      }
      if (pw !== pwConfirm) {
        enqueueSnackbar("Not Same Password", {
          variant: "warning",
        });
        return false;
      }
      if (!agree) {
        enqueueSnackbar(
          "Please Check the agreement of the terms and conditions",
          {
            variant: "warning",
          }
        );
        return false;
      }
      if (tabValue === 0) {
        result = await UserRegister({ name, email, password: pw, country });
      } else if (tabValue === 1) {
        if (!bsNum || !corName) {
          enqueueSnackbar("Please enter all the information", {
            variant: "warning",
          });
          return false;
        }
        result = await CoUserRegister({
          name,
          email,
          password: pw,
          country,
          corporate_name: corName,
          business_num: bsNum,
        });
      }
      if (result) {
        enqueueSnackbar("Register Done", {
          variant: "success",
        });
        router.push("/auth/login");
        return true;
      } else {
        enqueueSnackbar("Register Done", {
          variant: "warning",
        });
        return false;
      }
    } catch (err: any) {
      if (err.response.data.message === "중복된 이메일이 존재합니다.") {
        return enqueueSnackbar("Existing Email", { variant: "error" });
      } else {
        console.error(err);
        return enqueueSnackbar("Server Error", { variant: "error" });
      }
    }
  };

  const initialRegisterForm = () => {
    setName("");
    setCorName("");
    setbsNum("");
    setEmail("");
    setCountry("");
    setCode("");
    setPw("");
    setPwConfirm("");
    setSended(false);
    setVerified(false);
    setAgree(false);
  };

  return (
    <AuthContainer>
      <AuthCard maxWidth={400} mx={"auto"}>
        <Stack direction={"column"}>
          <Typography variant="h1" fontSize={24} fontWeight={700} mb={1}>
            Hi!
          </Typography>
          <Typography
            variant="body1"
            fontSize={"small"}
            color={grey[500]}
            mb={2}
          >
            Create New Account
          </Typography>
          <Box sx={{ borderBottom: 1, borderColor: "divider" }} mb={2}>
            <RegisterTabs
              value={tabValue}
              onChange={handleChangeJoinType}
              variant="fullWidth"
            >
              <RegisterTab label="Individual" {...a11yProps(0)} />
              <RegisterTab label="Corporate" {...a11yProps(1)} />
            </RegisterTabs>
          </Box>
          <Stack direction={"column"} gap={1}>
            <TextField
              label="Name"
              type="text"
              autoComplete="userName"
              variant="standard"
              name="name"
              value={name ? name : ""}
              onChange={handleChangeRegisterField}
            />
            <TabPanel value={tabValue} index={1}>
              <TextField
                label="Corporate Name"
                type="text"
                autoComplete="CorporateName"
                variant="standard"
                name="corName"
                value={corName ? corName : ""}
                onChange={handleChangeRegisterField}
              />
              <TextField
                label="Business Number"
                type="text"
                autoComplete="BusinessNumber"
                variant="standard"
                name="bsNum"
                value={bsNum ? bsNum : ""}
                onChange={handleChangeRegisterField}
              />
            </TabPanel>
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
            <FormControl variant="standard">
              <InputLabel htmlFor="userEmail">Email</InputLabel>
              <Input
                id="userEmail"
                type={"text"}
                sx={{ height: "40px" }}
                value={email ? email : ""}
                name="email"
                onChange={handleChangeRegisterField}
                readOnly={sended}
                endAdornment={
                  <InputAdornment position="end">
                    <Button
                      variant="contained"
                      onClick={handleClicSendEmail}
                      sx={{ py: 0.5, width: "80px" }}
                      disabled={sended}
                    >
                      SEND
                    </Button>
                  </InputAdornment>
                }
              />
            </FormControl>
            {sended && (
              <FormControl variant="standard">
                <InputLabel htmlFor="verifyCode">Verify Code</InputLabel>
                <Input
                  id="verifyCode"
                  type={"text"}
                  name="code"
                  sx={{ height: "40px" }}
                  value={code ? code : ""}
                  onChange={handleChangeRegisterField}
                  endAdornment={
                    <InputAdornment position="end">
                      <Button
                        variant="contained"
                        onClick={handleClickVerified}
                        disabled={verified}
                        sx={{ py: 0.5, width: "80px" }}
                      >
                        Verify
                      </Button>
                    </InputAdornment>
                  }
                />
              </FormControl>
            )}
            <TextField
              label="Password"
              type="password"
              autoComplete="new-password"
              variant="standard"
              name="pw"
              value={pw ? pw : ""}
              onChange={handleChangeRegisterField}
            />
            <TextField
              label="Password Confirm"
              type="password"
              autoComplete="password-confirm"
              variant="standard"
              name="pwConfirm"
              value={pwConfirm ? pwConfirm : ""}
              onChange={handleChangeRegisterField}
            />
            <Stack direction={"row"} alignItems={"center"} mb={7}>
              <AuthCheckBox
                {...Checklabel}
                icon={<AiOutlineCheckCircle />}
                checkedIcon={<AiFillCheckCircle />}
                checked={agree}
                onChange={(e: React.ChangeEvent<HTMLInputElement>) => {
                  if (e.target.checked) {
                    setAgree(true);
                  } else {
                    setAgree(false);
                  }
                }}
              />
              <Typography variant="body1" fontSize={"small"} color={grey[500]}>
                I Read and Agree to
                <Link href={"/terms"} target="_blank" sx={{ ml: 0.5 }}>
                  Terms
                </Link>
              </Typography>
            </Stack>
            <Button variant="contained" onClick={handleRegister}>
              JOIN
            </Button>
          </Stack>
        </Stack>
      </AuthCard>
    </AuthContainer>
  );
}
