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
import { useState } from "react";
import { useAuth } from "@/contexts/auth.context";
import { redirect } from "next/navigation";
import AccountListTitle from "@/components/account/AccountListTitle";
import AccountList, {
  AccountListHead,
  AccountListRow,
  AccountTd,
} from "@/components/account/AccountList";
import AccountNoList from "@/components/account/AccountNoList";

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
    corporate_name?: string;
    business_num?: string;
  };
}
interface Props extends DataProps {
  id: string;
}

export default function AccountContainer({ id, data }: Props) {
  const { user } = useAuth();

  if (!user || decodeURI(decodeURIComponent(id)) !== user?.email) {
    redirect("/");
  }

  const [info, setInfo] = useState<DataProps | null>(null);

  const [name, setName] = useState<string>(data.name);
  const [pw, setPw] = useState<string>(data.password);
  const [country, setCountry] = useState<string>(data.country);

  const [isCor, setIsCor] = useState<boolean>(false);
  const [corName, setCorName] = useState<string>(
    data.corporate_name ? data.corporate_name : ""
  );
  const [bsNum, setBsNum] = useState<string>(
    data.business_num ? data.business_num : ""
  );

  const handleChangeAcount = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    if (name === "name") setName(value);
    if (name === "pw") setPw(value);
    if (name === "corName") setCorName(value);
    if (name === "bsNum") setBsNum(value);
  };

  const handleSelect = (event: SelectChangeEvent) => {
    setCountry(event.target.value);
  };

  return (
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
              <Button variant="contained" fullWidth sx={{ height: 40 }}>
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
  );
}
