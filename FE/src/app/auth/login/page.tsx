"use client";
import {
  AuthCard,
  AuthContainer,
  AuthLoginBtn,
} from "@/components/auth/styled";
import {
  Box,
  Button,
  Divider,
  Input,
  Link,
  Stack,
  Typography,
} from "@mui/material";
import { blue, grey } from "@mui/material/colors";
import Image from "next/image";
import { BsArrowRightShort } from "react-icons/bs";

export default function LoginPage() {
  return (
    <AuthContainer>
      <AuthCard maxWidth={800} mx={"auto"}>
        <Stack
          direction={"row"}
          divider={<Divider orientation="vertical" flexItem />}
          spacing={4}
        >
          <Stack direction={"column"} flex={1} gap={9}>
            <Stack direction={"column"} alignItems={"flex-start"} gap={1}>
              <Typography fontSize={24} fontWeight={700}>
                Welcome to
              </Typography>
              <Box position={"relative"} width={300} height={24}>
                <Image src={"/logo.svg"} alt="logo" layout="fill" priority />
              </Box>
            </Stack>

            <Box>
              <Typography
                variant="body1"
                color={grey[500]}
                lineHeight={1.5}
                fontSize={"small"}
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
            <Stack direction="column" gap={2} mb={4}>
              <Input placeholder="Email" />
              <Input type="password" placeholder="Password" />
            </Stack>
            <AuthLoginBtn variant="contained" endIcon={<BsArrowRightShort />}>
              SIGN IN
            </AuthLoginBtn>
            <Stack direction={"row"} gap={1} alignItems="center">
              <Link
                href="/auth/findPassword"
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
