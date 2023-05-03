"use client";
import { Box, Button, IconButton, Stack } from "@mui/material";
import { deepPurple, grey, red } from "@mui/material/colors";
import Image from "next/image";
import Link from "next/link";
import { StyledButton, StyledLink } from "./styles";
import { FiSearch } from "react-icons/fi";

export default function Header() {
  return (
    <Stack
      width={1}
      height={"60px"}
      direction={"row"}
      justifyContent={"center"}
      borderBottom={1}
      borderColor={deepPurple[100]}
      position={"fixed"}
      bgcolor={"white"}
      alignItems={"center"}
      top={0}
      left={0}
    >
      <Stack
        width={"calc(100% - 32px)"}
        maxWidth={"1800px"}
        direction={"row"}
        alignItems={"center"}
        justifyContent={"space-between"}
      >
        <Link href={"/"}>
          <Image
            src={"/logo.svg"}
            alt="logo"
            width={180}
            height={14}
            priority
          />
        </Link>

        <Stack
          component={"nav"}
          direction={"row"}
          gap={4}
          alignItems={"center"}
          color={grey[500]}
          fontSize={14}
        >
          <StyledButton>
            <FiSearch />
          </StyledButton>
          <StyledLink href={"/"}>INDUSTRY</StyledLink>
          <StyledLink href={"/"}>SERVICE</StyledLink>
          <StyledLink href={"/"}>TERMS</StyledLink>
          <Button variant="contained">SIGN IN</Button>
        </Stack>
      </Stack>
    </Stack>
  );
}
