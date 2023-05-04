"use client";

import {
  Box,
  Button,
  IconButton,
  Input,
  Stack,
  Typography,
} from "@mui/material";
import { AiOutlineCloseCircle } from "react-icons/ai";
import { SearchCloseBtn } from "./styles";
import { deepPurple } from "@mui/material/colors";
import { FiSearch } from "react-icons/fi";

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
        maxWidth={"1800px"}
        direction={"column"}
        justifyContent={"space-between"}
      >
        <Stack direction={"row"} gap={1}>
          <Input
            placeholder="Search Company or CEO"
            sx={{ flex: 1, px: 2, borderColor: deepPurple[300] }}
          />
          <Button variant="contained">
            <FiSearch style={{ fontSize: "1rem" }} />
          </Button>
        </Stack>
      </Stack>
    </Stack>
  );
}
