"use client";

import { useAuth } from "@/contexts/auth.context";
import { Logout } from "@mui/icons-material";
import {
  Avatar,
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
  const { user, signOut } = useAuth();
  const router = useRouter();
  const handleGotoAccount = () => {
    if (!user) return;
    if (user.data.user_name) {
      router.push(`/account/individual/${user?.email}`);
    } else if (user.data.coruser_name) {
      router.push(`/account/corporate/${user?.email}`);
    }
  };
  const userState = !user
    ? "not user"
    : user.data.user_name
    ? user.data.user_name
    : user.data.coruser_name
    ? user.data.coruser_name
    : "unknown";
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
      {user && (
        <>
          <Stack
            direction={"row"}
            pb={1}
            borderBottom={1}
            borderColor={grey[200]}
          >
            <Stack direction={"column"}>
              <Typography
                variant="body1"
                fontSize={"small"}
                mb={1}
                color={grey[500]}
              >
                welcome!
              </Typography>
              <Stack
                direction={"row"}
                alignItems={"center"}
                gap={1}
                onClick={handleGotoAccount}
              >
                <Avatar /> {userState}
              </Stack>
            </Stack>
          </Stack>
        </>
      )}
      <List
        component="nav"
        subheader={
          <ListSubheader
            component="div"
            id="nested-list-subheader"
            sx={{ px: 0 }}
          >
            Welcome to Sentinel Korea KYC
          </ListSubheader>
        }
      >
        <ListItemButton sx={{ px: 0 }} component="a" href={"/industry"}>
          <ListItemText primary="INDUSTRY" />
        </ListItemButton>
        <ListItemButton sx={{ px: 0 }} component="a" href={"/service"}>
          <ListItemText primary="SERVICE" />
        </ListItemButton>
        <ListItemButton sx={{ px: 0 }} component="a" href={"/terms"}>
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
        {user ? (
          <>
            <Button
              variant="outlined"
              startIcon={<Logout fontSize="small" />}
              onClick={signOut}
            >
              Logout
            </Button>
          </>
        ) : (
          <>
            <Typography fontSize="small" color={grey[500]}>
              Is this your first time?
            </Typography>
            <Link
              href={"/auth/login"}
              sx={{ textDecoration: "none", fontWeight: 700 }}
            >
              Sign In
            </Link>
          </>
        )}
      </Stack>
    </Stack>
  );
}
