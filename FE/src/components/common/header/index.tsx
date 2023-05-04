"use client";
import {
  Box,
  Button,
  Hidden,
  IconButton,
  Stack,
  useTheme,
} from "@mui/material";
import { deepPurple, grey, red } from "@mui/material/colors";
import Image from "next/image";
import Link from "next/link";
import { Spacer, StyledButton, StyledLink } from "./styles";
import { FiSearch } from "react-icons/fi";
import { HiBars3BottomRight } from "react-icons/hi2";
import useMediaQuery from "@mui/material/useMediaQuery";
import HeaderSearch from "./HeaderSearch";
import { useState } from "react";
import { useRouter } from "next/navigation";
import MoHeaderMemu from "./MoHeaderMemu";

export default function Header() {
  const router = useRouter();
  const theme = useTheme();
  const matches = useMediaQuery(theme.breakpoints.up("md"));

  const [searchOpen, setSearchOpen] = useState<boolean>(false);
  const [moMenuOpen, setMoMenuOpen] = useState<boolean>(false);

  const handleSearchOpen = () => {
    setSearchOpen(!searchOpen);
  };

  const handleGotoLogin = () => {
    router.push("/auth/login");
  };

  return (
    <>
      <Stack
        width={1}
        height={60}
        direction={"row"}
        justifyContent={"center"}
        borderBottom={1}
        borderColor={deepPurple[100]}
        position={"fixed"}
        bgcolor={"white"}
        alignItems={"center"}
        top={0}
        left={0}
        zIndex={999}
      >
        <Stack
          width={"calc(100% - 32px)"}
          maxWidth={"1586px"}
          direction={"row"}
          alignItems={"center"}
          justifyContent={"space-between"}
        >
          <Link href={"/"}>
            <Image
              src={"/logo.svg"}
              alt="logo"
              width={matches ? 180 : 130}
              height={14}
              priority
            />
          </Link>

          <Stack
            component={"nav"}
            direction={"row"}
            gap={matches ? 4 : 1}
            alignItems={"center"}
            color={grey[500]}
            fontSize={14}
          >
            <StyledButton onClick={handleSearchOpen}>
              <FiSearch />
            </StyledButton>
            <Hidden mdDown>
              <>
                <StyledLink href={"/"}>INDUSTRY</StyledLink>
                <StyledLink href={"/"}>SERVICE</StyledLink>
                <StyledLink href={"/"}>TERMS</StyledLink>
                <Button variant="contained" onClick={handleGotoLogin}>
                  SIGN IN
                </Button>
              </>
            </Hidden>
            <Hidden mdUp>
              <IconButton onClick={() => setMoMenuOpen(!moMenuOpen)}>
                <HiBars3BottomRight />
              </IconButton>
            </Hidden>
          </Stack>
        </Stack>
      </Stack>
      {searchOpen && <HeaderSearch />}
      {moMenuOpen && (
        <Hidden mdUp>
          <MoHeaderMemu />
        </Hidden>
      )}
      <Spacer />
    </>
  );
}
