"use client";

import { Stack, PaginationItem, useMediaQuery, useTheme } from "@mui/material";
import KeyboardArrowLeftIcon from "@mui/icons-material/KeyboardArrowLeft";
import KeyboardDoubleArrowLeftIcon from "@mui/icons-material/KeyboardDoubleArrowLeft";
import KeyboardArrowRightIcon from "@mui/icons-material/KeyboardArrowRight";
import KeyboardDoubleArrowRightIcon from "@mui/icons-material/KeyboardDoubleArrowRight";
import { StyledPagination } from "./styles";

export default function PaginationBox({
  page,
  count,
  onChange,
}: {
  page?: number;
  count?: number;
  onChange: (event: React.ChangeEvent<unknown>, value: number) => void;
}) {
  const theme = useTheme();
  const matches = useMediaQuery(theme.breakpoints.up("md"));
  return (
    <Stack spacing={0} justifyContent={"center"} alignItems={"center"}>
      <StyledPagination
        count={count ? count : 10}
        page={page ? page : 1}
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
        onChange={onChange}
      />
    </Stack>
  );
}
