"use client";
import {
  Avatar,
  Button,
  Divider,
  Hidden,
  IconButton,
  ListItemIcon,
  Menu,
  MenuItem,
  Stack,
  Typography,
  useTheme,
} from "@mui/material";
import { deepPurple, grey } from "@mui/material/colors";
import Image from "next/image";
import Link from "next/link";
import { Spacer, StyledButton, StyledLink } from "./styles";
import { FiSearch } from "react-icons/fi";
import { HiBars3BottomRight } from "react-icons/hi2";
import useMediaQuery from "@mui/material/useMediaQuery";
import HeaderSearch from "./HeaderSearch";
import { useEffect, useState } from "react";
import { usePathname, useRouter } from "next/navigation";
import MoHeaderMemu from "./MoHeaderMemu";
import { Settings, Logout } from "@mui/icons-material";
import { useAuth } from "@/contexts/auth.context";

export default function Header() {
  const router = useRouter();
  const pathname = usePathname();
  const theme = useTheme();
  const matches = useMediaQuery(theme.breakpoints.up("md"));

  const { user, signOut } = useAuth();

  const [searchOpen, setSearchOpen] = useState<boolean>(false);
  const [moMenuOpen, setMoMenuOpen] = useState<boolean>(false);

  const [anchorEl, setAnchorEl] = useState<null | HTMLElement>(null);
  const open = Boolean(anchorEl);

  const handleSearchOpen = () => {
    setSearchOpen(!searchOpen);
    setMoMenuOpen(false);
  };

  const handleMoMenuOpen = () => {
    setMoMenuOpen(!moMenuOpen);
    setSearchOpen(false);
  };

  useEffect(() => {
    setSearchOpen(false);
    setMoMenuOpen(false);
  }, [pathname]);

  const handleClickAuthButton = (event: React.MouseEvent<HTMLElement>) => {
    if (user) {
      setAnchorEl(event.currentTarget);
    } else {
      router.push("/auth/login");
    }
  };
  const handleCloseMenu = () => {
    setAnchorEl(null);
  };

  const handleClickAccount = () => {
    if (!user) return;
    if (user.data.user_name) {
      router.push(`/account/individual/${user?.email}`);
    } else if (user.data.coruser_name) {
      router.push(`/account/corporate/${user?.email}`);
    }
  };

  const isIndustry = pathname === "/industry";
  const isService = pathname === "/service";
  const isTerms = pathname === "/terms";

  const userState = !user
    ? "SIGN IN"
    : user.data.user_name
    ? user.data.user_name
    : user.data.coruser_name
    ? user.data.coruser_name
    : "unknown";

  return (
    <>
      <Stack
        width={"100vw"}
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
                <StyledLink href={"/industry"} isActive={isIndustry}>
                  INDUSTRY
                </StyledLink>
                <StyledLink href={"/service"} isActive={isService}>
                  SERVICE
                </StyledLink>
                <StyledLink href={"/terms"} isActive={isTerms}>
                  TERMS
                </StyledLink>
                <Button variant="contained" onClick={handleClickAuthButton}>
                  {userState}
                </Button>
                <Menu
                  anchorEl={anchorEl}
                  id="account-menu"
                  open={open}
                  onClose={handleCloseMenu}
                  onClick={handleCloseMenu}
                  PaperProps={{
                    elevation: 0,
                    sx: {
                      minWidth: "200px",
                      overflow: "visible",
                      filter: "drop-shadow(0px 2px 8px rgba(0,0,0,0.32))",
                      mt: 1.5,
                      "& .MuiAvatar-root": {
                        width: 32,
                        height: 32,
                        ml: -0.5,
                        mr: 1,
                      },
                      "&:before": {
                        content: '""',
                        display: "block",
                        position: "absolute",
                        top: 0,
                        right: 14,
                        width: 10,
                        height: 10,
                        bgcolor: "background.paper",
                        transform: "translateY(-50%) rotate(45deg)",
                        zIndex: 0,
                      },
                    },
                  }}
                  transformOrigin={{ horizontal: "right", vertical: "top" }}
                  anchorOrigin={{ horizontal: "right", vertical: "bottom" }}
                >
                  <MenuItem onClick={handleClickAccount}>
                    <Stack direction={"column"}>
                      <Typography
                        variant="body1"
                        fontSize={"small"}
                        mb={1}
                        color={grey[500]}
                      >
                        welcome!
                      </Typography>
                      <Stack direction={"row"} alignItems={"center"}>
                        <Avatar /> {userState}
                      </Stack>
                    </Stack>
                  </MenuItem>
                  <Divider />
                  <MenuItem onClick={handleCloseMenu}>
                    <ListItemIcon>
                      <Settings fontSize="small" />
                    </ListItemIcon>
                    My Service
                  </MenuItem>
                  <MenuItem onClick={signOut}>
                    <ListItemIcon>
                      <Logout fontSize="small" />
                    </ListItemIcon>
                    Logout
                  </MenuItem>
                </Menu>
              </>
            </Hidden>
            <Hidden mdUp>
              <IconButton onClick={handleMoMenuOpen}>
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
