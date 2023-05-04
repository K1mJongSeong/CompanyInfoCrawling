"use client";

import {
  AuthContainer,
  AuthCard,
  RegisterTabs,
  RegisterTab,
  AuthCheckBox,
} from "@/components/auth/styled";
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
  NativeSelect,
  Select,
  SelectChangeEvent,
  Stack,
  TextField,
  Typography,
  useTheme,
} from "@mui/material";
import { grey } from "@mui/material/colors";
import { useSnackbar } from "notistack";
import { useState } from "react";
import { AiFillCheckCircle, AiOutlineCheckCircle } from "react-icons/ai";

interface TabPanelProps {
  children?: React.ReactNode;
  index: number;
  value: number;
}

function TabPanel(props: TabPanelProps) {
  const { children, value, index, ...other } = props;

  return (
    <div
      role="tabpanel"
      hidden={value !== index}
      id={`full-width-tabpanel-${index}`}
      {...other}
    >
      {value === index && (
        <Stack direction={"column"} gap={1}>
          {children}
        </Stack>
      )}
    </div>
  );
}

function a11yProps(index: number) {
  return {
    id: `simple-tab-${index}`,
    "aria-controls": `simple-tabpanel-${index}`,
  };
}

const Checklabel = { inputProps: { "aria-label": "Term Checkbox" } };

export default function RegisterContainer() {
  const [value, setValue] = useState<number>(0);
  const handleChange = (event: React.SyntheticEvent, newValue: number) => {
    setValue(newValue);
  };
  const [age, setAge] = useState("");

  const handleSelect = (event: SelectChangeEvent) => {
    setAge(event.target.value);
  };

  const { enqueueSnackbar } = useSnackbar();

  const { verifyEmail } = new VerifyAuth();

  const [email, setEmail] = useState<string>("");
  const [code, setCode] = useState<string>("");

  const [sended, setSended] = useState<boolean>(false);
  const [verified, setVerified] = useState<boolean>(false);

  const handleClicSendEmail = async () => {
    const result = await verifyEmail(email, enqueueSnackbar);
    if (result) {
      setSended(true);
    }
  };

  const handleClickVerified = () => {
    if (!setCode) {
      enqueueSnackbar("Enter Code", { variant: "warning" });
      return false;
    }
    enqueueSnackbar("Verified Code", { variant: "success" });
    setVerified(true);
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
              value={value}
              onChange={handleChange}
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
              onChange={(event: React.ChangeEvent<HTMLInputElement>) => {
                console.log(event.target.value);
              }}
            />
            <TabPanel value={value} index={1}>
              <TextField
                label="Corporate Name"
                type="text"
                autoComplete="CorporateName"
                variant="standard"
                onChange={(event: React.ChangeEvent<HTMLInputElement>) => {
                  console.log(event.target.value);
                }}
              />
              <TextField
                label="Business Number"
                type="text"
                autoComplete="BusinessNumber"
                variant="standard"
                onChange={(event: React.ChangeEvent<HTMLInputElement>) => {
                  console.log(event.target.value);
                }}
              />
            </TabPanel>
            <FormControl variant="standard">
              <InputLabel id="demo-simple-select-standard-label">
                Select Country
              </InputLabel>
              <Select value={age} onChange={handleSelect} label="Age">
                <MenuItem value="">
                  <em>None</em>
                </MenuItem>
                <MenuItem value={10}>Ten</MenuItem>
                <MenuItem value={20}>Twenty</MenuItem>
                <MenuItem value={30}>Thirty</MenuItem>
              </Select>
            </FormControl>
            <FormControl variant="standard">
              <InputLabel htmlFor="userEmail">Email</InputLabel>
              <Input
                id="userEmail"
                type={"text"}
                sx={{ height: "40px" }}
                value={email ? email : ""}
                onChange={(event: React.ChangeEvent<HTMLInputElement>) => {
                  setEmail(event.target.value);
                }}
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
                  sx={{ height: "40px" }}
                  value={code ? code : ""}
                  onChange={(e: React.ChangeEvent<HTMLInputElement>) => {
                    setCode(e.target.value);
                  }}
                  endAdornment={
                    <InputAdornment position="end">
                      <Button
                        variant="contained"
                        onClick={handleClickVerified}
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
              onChange={(event: React.ChangeEvent<HTMLInputElement>) => {
                console.log(event.target.value);
              }}
            />
            <TextField
              label="Password Confirm"
              type="password"
              autoComplete="password-confirm"
              variant="standard"
              onChange={(event: React.ChangeEvent<HTMLInputElement>) => {
                console.log(event.target.value);
              }}
            />
            <Stack direction={"row"} alignItems={"center"} mb={7}>
              <AuthCheckBox
                {...Checklabel}
                icon={<AiOutlineCheckCircle />}
                checkedIcon={<AiFillCheckCircle />}
              />
              <Typography variant="body1" fontSize={"small"} color={grey[500]}>
                I Read and Agree to
                <Link href={"/"} target="_blank" sx={{ ml: 0.5 }}>
                  Terms
                </Link>
              </Typography>
            </Stack>
            <Button variant="contained">JOIN</Button>
          </Stack>
        </Stack>
      </AuthCard>
    </AuthContainer>
  );
}
