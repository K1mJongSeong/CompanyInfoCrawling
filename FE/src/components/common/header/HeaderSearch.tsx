"use client";

import { Button, Stack } from "@mui/material";
import { FiSearch } from "react-icons/fi";
import { SearchInput } from "./styles";
import { useRouter } from "next/navigation";
import { GotoSearch } from "@/service/search_service";
import { useSnackbar } from "notistack";
import { useState } from "react";

export default function HeaderSearch() {
  const router = useRouter();
  const { enqueueSnackbar } = useSnackbar();
  const [value, setValue] = useState<string>("");
  const handleChangeSearchValue = (e: React.ChangeEvent<HTMLInputElement>) => {
    setValue(e.target.value);
  };
  const handleSubmit = (e: React.FormEvent) => {
    GotoSearch({ e, value, router, enqueueSnackbar });
  };
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
        <Stack component={"form"} onSubmit={handleSubmit} direction={"row"} gap={1}>
          <SearchInput
            placeholder="Search Company or CEO"
            sx={{ flex: 1, px: 2 }}
            value={value?value:""}
            onChange={handleChangeSearchValue}
          />
          <Button type="submit" variant="contained">
            <FiSearch style={{ fontSize: "1rem" }} />
          </Button>
        </Stack>
      </Stack>
    </Stack>
  );
}
