"use client";

import { AuthContainer, AuthCard } from "@/components/auth/styled";
import { VariantType, useSnackbar } from "notistack";
import {
  Avatar,
  Box,
  Button,
  FormControl,
  Input,
  InputAdornment,
  InputLabel,
  Stack,
  TextField,
  Typography,
} from "@mui/material";
import { grey } from "@mui/material/colors";
import { useState } from "react";
import VerifyAuth from "@/utils/auth/verified";
import { redirect, usePathname, useRouter } from "next/navigation";
import Image from "next/image";

export default function FindPWContainer() {
  const { enqueueSnackbar } = useSnackbar();

  const router = useRouter();
  const pathname = usePathname();
  const isFirst = pathname === "/auth/findPassword/1";
  const isSec = pathname === "/auth/findPassword/2";
  const isThird = pathname === "/auth/findPassword/3";

  const { verifyEmail } = new VerifyAuth();

  //** first */
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

  //** second */
  const [pw, setPw] = useState<string>("");
  const [pwConfirm, setPwConfirm] = useState<string>("");

  //** Third */

  const handleClickButton = () => {
    if (isFirst) {
      router.push("/auth/findPassword/2");
    }
    if (isSec) {
      if (!pw) return enqueueSnackbar("Enter Password", { variant: "warning" });
      if (!pwConfirm)
        return enqueueSnackbar("Enter Password Confirm", {
          variant: "warning",
        });
      if (pw !== pwConfirm) {
        return enqueueSnackbar("Not Same", {
          variant: "warning",
        });
      }
      router.push("/auth/findPassword/3");
    }
    if (isThird) {
      router.push("/auth/login");
    }
  };

  return (
    <AuthContainer>
      <AuthCard maxWidth={400} mx={"auto"}>
        <Stack direction={"column"}>
          <Typography variant="h1" fontSize={24} fontWeight={700} mb={1}>
            {isFirst && "Forgot your PW?"}
            {isSec && "Reset your PW"}
            {isThird && "DONE!"}
          </Typography>
          <Typography
            variant="body1"
            fontSize={"small"}
            color={grey[500]}
            mb={5}
          >
            {isFirst && (
              <>
                It’s Okay! reset your password <br /> Enter your Email Account
              </>
            )}
            {isSec && "Enter yout new Password"}
            {isThird && (
              <>
                Your password has been reset sucessfully!
                <br />
                Now Sogn In with your new password{" "}
              </>
            )}
          </Typography>
          <Stack direction={"column"} gap={1} mb={10}>
            {isFirst && (
              <>
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
              </>
            )}
            {isSec && (
              <>
                <TextField
                  label="Password"
                  type="password"
                  autoComplete="new-password"
                  variant="standard"
                  value={pw ? pw : ""}
                  onChange={(event: React.ChangeEvent<HTMLInputElement>) => {
                    setPw(event.target.value);
                  }}
                />
                <TextField
                  label="Password Confirm"
                  type="password"
                  autoComplete="new-password-confirm"
                  variant="standard"
                  value={pwConfirm ? pwConfirm : ""}
                  onChange={(event: React.ChangeEvent<HTMLInputElement>) => {
                    setPwConfirm(event.target.value);
                  }}
                />
              </>
            )}
            {isThird && (
              <Box
                width={1}
                maxWidth={170}
                height={170}
                position={"relative"}
                mx={"auto"}
              >
                <Image
                  src={"/assets/images/lock_icon.svg"}
                  alt="lock"
                  layout="fill"
                />
              </Box>
            )}
          </Stack>
          <Button
            variant="contained"
            disabled={isFirst && !verified}
            onClick={handleClickButton}
          >
            {isFirst && "NEXT"}
            {isSec && "RESET"}
            {isThird && "Sign In"}
          </Button>
        </Stack>
      </AuthCard>
    </AuthContainer>
  );
}
