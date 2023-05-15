/* eslint-disable react-hooks/exhaustive-deps */
"use client";
import {
  AcountContainer,
  AcountCard,
  AcountDisabledFiled,
} from "@/components/account/styles";
import {
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
import { blue } from "@mui/material/colors";
import Countries from "@/data/countries.json";
import uuid from "react-uuid";
import { InCountry } from "@/service/auth_service";
import { useEffect, useState } from "react";
import { useAuth } from "@/contexts/auth.context";
import { redirect } from "next/navigation";

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
          <Stack direction={"column"} gap={2}>
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
        </Stack>
      </AcountCard>
    </AcountContainer>
  );
}
