"use client";

import {
  Box,
  Button,
  Link,
  List,
  ListItemButton,
  ListItemText,
  ListSubheader,
  Stack,
  Typography,
} from "@mui/material";
import { grey } from "@mui/material/colors";
import { useRouter } from "next/navigation";

export default function MoHeaderMemu() {
  const router = useRouter();
  const handleGotoLogin = () => {
    router.push("/auth/login");
  };

  return (
    <Stack
      direction={"column"}
      width={1}
      height={"calc(100vh - 60px)"}
      position={"fixed"}
      top={60}
      right={0}
      zIndex={997}
      bgcolor="white"
      px={2}
      py={2}
      gap={2}
    >
      <List
        component="nav"
        subheader={
          <ListSubheader component="div" id="nested-list-subheader" sx={{px:0}}>
            Welcome to Sentinel Korea KYC
          </ListSubheader>
        }
      >
        <ListItemButton sx={{px:0}}  component="a" href={"/"}>
          <ListItemText primary="INDUSTRY" />
        </ListItemButton>
        <ListItemButton  sx={{px:0}} component="a" href={"/"}>
          <ListItemText primary="SERVICE" />
        </ListItemButton>
        <ListItemButton  sx={{px:0}} component="a" href={"/"}>
          <ListItemText primary="TERMS" />
        </ListItemButton>
      </List>
      <Stack
        direction={"row"}
        py={2}
        borderTop={1}
        gap={1}
        borderBottom={1}
        alignItems={"center"}
        justifyContent={"flex-end"}
        borderColor={grey[200]}
      >
        <Typography fontSize="small" color={grey[500]}>
          Is this your first time?
        </Typography>
        <Link
          href={"/auth/login"}
          sx={{ textDecoration: "none", fontWeight: 700 }}
        >
          Sign In
        </Link>
      </Stack>
    </Stack>
  );
}
