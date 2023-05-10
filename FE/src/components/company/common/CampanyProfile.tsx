"use client";

import {
  useMediaQuery,
  useTheme,
  Stack,
  Typography,
  Divider,
  Tooltip,
  Button,
} from "@mui/material";
import { grey } from "@mui/material/colors";
import { AiFillFileText } from "react-icons/ai";

interface Props {
  pdf?: boolean;
}

export default function CampanyProfile({ pdf }: Props) {
  const theme = useTheme();
  const matches = useMediaQuery(theme.breakpoints.up("md"));
  return (
    <Stack
      direction={matches ? "row" : "column"}
      width={1}
      py={3}
      px={2}
      border={"1px solid"}
      borderColor={"#a7a7ce;"}
      justifyContent={"space-between"}
      borderRadius={2}
      alignItems={"flex-end"}
      mb={4}
    >
      <Stack direction={"column"} gap={1} width={1}>
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
      {pdf && (
        <Button variant="contained" endIcon={<AiFillFileText />}>
          PDF
        </Button>
      )}
    </Stack>
  );
}
