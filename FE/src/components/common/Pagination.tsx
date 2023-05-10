"use client";

import { Stack, PaginationItem, useMediaQuery, useTheme } from "@mui/material";
import KeyboardArrowLeftIcon from "@mui/icons-material/KeyboardArrowLeft";
import KeyboardDoubleArrowLeftIcon from "@mui/icons-material/KeyboardDoubleArrowLeft";
import KeyboardArrowRightIcon from "@mui/icons-material/KeyboardArrowRight";
import KeyboardDoubleArrowRightIcon from "@mui/icons-material/KeyboardDoubleArrowRight";
import { StyledPagination } from "./styles";

export default function PaginationBox() {
  const theme = useTheme();
  const matches = useMediaQuery(theme.breakpoints.up("md"));
  return (
    <Stack spacing={0} justifyContent={"center"} alignItems={"center"}>
      <StyledPagination
        count={10}
        color="primary"
        renderItem={(item) => (
          <PaginationItem
            slots={{
              first: KeyboardDoubleArrowLeftIcon,
              previous: KeyboardArrowLeftIcon,
              next: KeyboardArrowRightIcon,
              last: KeyboardDoubleArrowRightIcon,
            }}
            {...item}
          />
        )}
        showFirstButton={matches}
        showLastButton={matches}
      />
    </Stack>
  );
}
