"use client";

import {
  useMediaQuery,
  useTheme,
  Stack,
  Typography,
  Divider,
  Tooltip,
} from "@mui/material";
import { grey } from "@mui/material/colors";

export default function CampanyProfile() {
  const theme = useTheme();
  const matches = useMediaQuery(theme.breakpoints.up("md"));
  return (
    <Stack
      direction={"column"}
      gap={1}
      width={1}
      py={3}
      px={2}
      border={"1px solid"}
      borderColor={"#a7a7ce;"}
      borderRadius={2}
      mb={3}
    >
      <Stack direction={"row"} mb={matches ? 0 : 1}>
        <Typography variant="h3" fontSize={"large"} fontWeight={"bold"}>
          COMPANY NAME
        </Typography>
      </Stack>
      <Stack
        direction={"row"}
        gap={matches ? 3 : 1}
        flexWrap={"wrap"}
        divider={<Divider orientation="vertical" flexItem />}
      >
        <Tooltip title="Ceo Name">
          <Typography variant="body1" fontSize={"14px"}>
            CEO NAME
          </Typography>
        </Tooltip>
        <Tooltip title="Business Number">
          <Typography variant="body1" fontSize={"14px"}>
            BUSINESS NUMBER
          </Typography>
        </Tooltip>
        <Tooltip title="Corparate From">
          <Typography variant="body1" fontSize={"14px"}>
            CORPARATE FROM
          </Typography>
        </Tooltip>
      </Stack>
      <Stack direction={"row"}>
        <Typography variant="body2" fontSize={"small"} color={grey[500]}>
          Establishment
        </Typography>
      </Stack>
    </Stack>
  );
}
