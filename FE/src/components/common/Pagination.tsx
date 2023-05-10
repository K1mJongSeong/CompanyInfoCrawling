"use client";

import { Stack, PaginationItem, Pagination } from "@mui/material";
import KeyboardArrowLeftIcon from "@mui/icons-material/KeyboardArrowLeft";
import KeyboardDoubleArrowLeftIcon from "@mui/icons-material/KeyboardDoubleArrowLeft";
import KeyboardArrowRightIcon from "@mui/icons-material/KeyboardArrowRight";
import KeyboardDoubleArrowRightIcon from "@mui/icons-material/KeyboardDoubleArrowRight";

export default function PaginationBox() {
  return (
    <Stack spacing={2} justifyContent={"center"} alignItems={"center"}>
      <Pagination
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
        showFirstButton
        showLastButton
      />
    </Stack>
  );
}
