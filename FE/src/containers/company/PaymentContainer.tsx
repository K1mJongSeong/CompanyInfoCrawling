"use client";
import CampanyProfile from "@/components/company/common/CampanyProfile";
import {
  BorderCompanyCard,
  StyledBtn,
} from "@/components/company/common/styles";
import {
  Box,
  Button,
  Stack,
  Typography,
  useMediaQuery,
  useTheme,
} from "@mui/material";
import { grey } from "@mui/material/colors";
import { FaPaperPlane } from "react-icons/fa";

export default function PaymentContainer() {
  const theme = useTheme();
  const matches = useMediaQuery(theme.breakpoints.up("md"));
  return (
    <>
      <CampanyProfile />
      <Stack direction={matches ? "row" : "column"} gap={matches ? 8 : 2}>
        <BorderCompanyCard>
          <Stack
            direction={"column"}
            justifyContent={"space-between"}
            height={1}
            gap={matches ? 5 : 2}
          >
            <Box>
              <Typography
                variant="h2"
                fontSize={"large"}
                fontWeight={"bold"}
                mb={2}
              >
                DD1
              </Typography>
              <Box bgcolor={"white"} py={1} px={3} borderRadius={1}>
                <ol>
                  <li>General company information</li>
                </ol>
              </Box>
            </Box>
            <Button variant="contained" fullWidth>
              $50
            </Button>
          </Stack>
        </BorderCompanyCard>
        <BorderCompanyCard>
          <Stack
            direction={"column"}
            justifyContent={"space-between"}
            height={1}
            gap={matches ? 5 : 2}
          >
            <Box>
              <Typography
                variant="h2"
                fontSize={"large"}
                fontWeight={"bold"}
                mb={2}
              >
                DD2
              </Typography>
              <Box bgcolor={"white"} py={1} px={3} borderRadius={1}>
                <ol>
                  <li>DD1</li>
                  <li>Media Search</li>
                  <li>Regulatory standing and litigation</li>
                </ol>
              </Box>
            </Box>
            <Button variant="contained" fullWidth>
              $300
            </Button>
          </Stack>
        </BorderCompanyCard>
        <BorderCompanyCard>
          <Stack direction={"column"} justifyContent={"space-between"}>
            <Box>
              <Typography variant="h2" fontSize={"large"} fontWeight={"bold"}>
                DD3
              </Typography>
              <Typography
                variant="body1"
                fontSize={"small"}
                color={grey[500]}
                mb={3}
              >
                (Further Inquiry) Service Fee
              </Typography>
            </Box>
            <Stack direction={"column"} gap={2}>
              <Stack
                direction="row"
                bgcolor={"white"}
                borderRadius={1}
                justifyContent={"space-between"}
                alignItems={"center"}
                pl={1}
              >
                <Typography variant="body1" color={grey[500]}>
                  Political exposure
                </Typography>

                <StyledBtn variant="contained">
                  <FaPaperPlane />
                </StyledBtn>
              </Stack>
              <Stack
                direction="row"
                bgcolor={"white"}
                borderRadius={1}
                justifyContent={"space-between"}
                alignItems={"center"}
                pl={1}
              >
                <Typography variant="body1" color={grey[500]}>
                  Source Inquire
                </Typography>

                <StyledBtn variant="contained">
                  <FaPaperPlane />
                </StyledBtn>
              </Stack>
              <Stack
                direction="row"
                bgcolor={"white"}
                borderRadius={1}
                justifyContent={"space-between"}
                alignItems={"center"}
                pl={1}
              >
                <Typography variant="body1" color={grey[500]}>
                  Site Visit
                </Typography>

                <StyledBtn variant="contained">
                  <FaPaperPlane />
                </StyledBtn>
              </Stack>
              <Stack
                direction="row"
                bgcolor={"white"}
                borderRadius={1}
                justifyContent={"space-between"}
                alignItems={"center"}
                pl={1}
              >
                <Typography variant="body1" color={grey[500]}>
                  Any Addition Question
                </Typography>

                <StyledBtn variant="contained">
                  <FaPaperPlane />
                </StyledBtn>
              </Stack>
            </Stack>
          </Stack>
        </BorderCompanyCard>
      </Stack>
    </>
  );
}
