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
import { useState } from "react";
import { useAuth } from "@/contexts/auth.context";

export default function LoginContainer() {
  const theme = useTheme();
  const matches = useMediaQuery(theme.breakpoints.up("md"));

  const [email, setEmail] = useState<string>("");
  const [pw, setPw] = useState<string>("");

  const { signIn, loading } = useAuth();

  const handleSubmitLogin = (e: React.FormEvent) => {
    e.preventDefault();
    signIn({ email, pw });
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
            <Stack
              component={"form"}
              onSubmit={handleSubmitLogin}
              direction="column"
              gap={1}
              mb={6}
            >
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
              <AuthLoginBtn
                type="submit"
                variant="contained"
                loading={loading}
                loadingPosition="end"
                endIcon={<BsArrowRightShort />}
              >
                SIGN IN
              </AuthLoginBtn>
            </Stack>
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
