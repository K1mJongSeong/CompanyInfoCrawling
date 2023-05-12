"use client";
import {
  AuthContainer,
  AuthCard,
  AuthLoginBtn,
} from "@/components/auth/styled";
import {
  Stack,
  Divider,
  Typography,
  Box,
  Input,
  Link,
  useTheme,
  useMediaQuery,
  TextField,
} from "@mui/material";
import { grey, blue } from "@mui/material/colors";
import { BsArrowRightShort } from "react-icons/bs";
import Image from "next/image";
import { useSnackbar } from "notistack";
import { useState } from "react";
import { Login } from "@/service/auth_service";

export default function LoginContainer() {
  const { enqueueSnackbar } = useSnackbar();

  const theme = useTheme();
  const matches = useMediaQuery(theme.breakpoints.up("md"));

  const [email, setEmail] = useState<string>("");
  const [pw, setPw] = useState<string>("");

  const handleLogin = async () => {
    try {
      if (!email || !pw) {
        return enqueueSnackbar("Enter All Login Field", { variant: "warning" });
      }
      const emailRule =
        /^[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*@[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*.[a-zA-Z]{2,3}$/i;

      if (!emailRule.test(email)) {
        return enqueueSnackbar("Not Email!", { variant: "warning" });
      }
      const result = await Login({ email, password: pw });
      if (result.message === "로그인에 성공했습니다.") {
        enqueueSnackbar("SUCCESS LOGIN", { variant: "success" });
      }
    } catch (err: any) {
      if (err.response.data.message === "존재하지 않는 아이디입니다.") {
        return enqueueSnackbar("Not User", { variant: "error" });
      } else {
        console.error(err);
        return enqueueSnackbar("Server Error", { variant: "error" });
      }
    }
  };

  return (
    <AuthContainer>
      <AuthCard maxWidth={matches ? 800 : "none"} mx={"auto"}>
        <Stack
          direction={matches ? "row" : "column"}
          divider={
            <Divider
              orientation={matches ? "vertical" : "horizontal"}
              flexItem
            />
          }
          spacing={4}
        >
          <Stack direction={"column"} flex={1} gap={matches ? 9 : 0}>
            <Stack
              direction={"column"}
              alignItems={"flex-start"}
              gap={matches ? 1 : 0}
            >
              <Typography fontSize={matches ? 24 : 18} fontWeight={700}>
                Welcome to
              </Typography>
              <Box position={"relative"} width={1} maxWidth={300} height={24}>
                <Image src={"/logo.svg"} alt="logo" layout="fill" priority />
              </Box>
            </Stack>

            <Box>
              <Typography
                variant="body1"
                color={grey[500]}
                lineHeight={1.5}
                fontSize={"small"}
                hidden={!matches}
              >
                {` Lorem Ipsum is simply dummy text of the printing and typesetting
              industry. Lorem Ipsum has been the industry's standard dummy text
              ever since the 1500s, when an unknown printer took a galley of
              type and scrambled it to make a type specimen book.`}
              </Typography>
            </Box>
          </Stack>
          <Box flex={1}>
            <Typography
              variant="body1"
              color={grey[500]}
              fontSize={"medium"}
              fontWeight={700}
              lineHeight={1.5}
              mb={2.5}
            >
              Please enter your Email and
              <br />
              password to SIGN IN
            </Typography>
            <Stack direction="column" gap={1} mb={4}>
              <TextField
                label="Email"
                type="text"
                autoComplete="email-id"
                variant="standard"
                value={email ? email : ""}
                onChange={(event: React.ChangeEvent<HTMLInputElement>) => {
                  setEmail(event.target.value);
                }}
              />
              <TextField
                label="Password"
                type="password"
                autoComplete="current-password"
                variant="standard"
                value={pw ? pw : ""}
                onChange={(event: React.ChangeEvent<HTMLInputElement>) => {
                  setPw(event.target.value);
                }}
              />
            </Stack>
            <AuthLoginBtn
              onClick={handleLogin}
              variant="contained"
              endIcon={<BsArrowRightShort />}
            >
              SIGN IN
            </AuthLoginBtn>
            <Stack direction={"row"} gap={1} alignItems="center">
              <Link
                href="/auth/findPassword/1"
                fontSize="small"
                color={blue[400]}
              >
                forgot PW?
              </Link>
              /
              <Link href="/auth/register" fontSize="small" color={blue[400]}>
                Register
              </Link>
            </Stack>
          </Box>
        </Stack>
      </AuthCard>
    </AuthContainer>
  );
}
