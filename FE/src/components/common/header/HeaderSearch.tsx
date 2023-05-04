"use client";

import { Button, Input, Stack } from "@mui/material";
import { deepPurple } from "@mui/material/colors";
import { FiSearch } from "react-icons/fi";
import { SearchInput } from "./styles";

export default function HeaderSearch() {
  return (
    <Stack
      direction={"row"}
      position={"fixed"}
      bgcolor={"white"}
      width={1}
      py={2}
      boxShadow={"4px 4px 20px rgba(23,33,122,0.3)"}
      top={60}
      left={0}
      alignItems={"center"}
      justifyContent={"center"}
      zIndex={997}
    >
      <Stack
        width={"calc(100% - 32px)"}
        maxWidth={"1586px"}
        direction={"column"}
        justifyContent={"space-between"}
      >
        <Stack direction={"row"} gap={1}>
          <SearchInput
            placeholder="Search Company or CEO"
            sx={{ flex: 1, px: 2 }}
          />
          <Button variant="contained">
            <FiSearch style={{ fontSize: "1rem" }} />
          </Button>
        </Stack>
      </Stack>
    </Stack>
  );
}
