"use client";

import { GotoSearch } from "@/service/search_service";
import { Box, Button, Stack, useMediaQuery, useTheme } from "@mui/material";
import { grey } from "@mui/material/colors";
import { useRouter } from "next/navigation";
import { useSnackbar } from "notistack";
import { useEffect, useState } from "react";
import { FiSearch } from "react-icons/fi";
import { MainStyledInput } from "../main/styled";
import { SearchTopBgBox } from "./styles";

export default function SearchTop({ searchValue }: { searchValue: string }) {
  const router = useRouter();
  const { enqueueSnackbar } = useSnackbar();
  const theme = useTheme();
  const matches = useMediaQuery(theme.breakpoints.up("md"));
  const [value, setValue] = useState<string>("");
  const handleChangeSearchValue = (e: React.ChangeEvent<HTMLInputElement>) => {
    setValue(e.target.value);
  };
  const handleSubmit = (e: React.FormEvent) => {
    GotoSearch({ e, value, router, enqueueSnackbar });
  };

  useEffect(() => {
    setValue(searchValue);
  }, [searchValue]);
  return (
    <Box position={"relative"}>
      <SearchTopBgBox />
      <Stack
        maxWidth={1388}
        component="form"
        position={"absolute"}
        top={"50%"}
        left={"50%"}
        onSubmit={handleSubmit}
        width={"calc(100% - 32px)"}
        height={70}
        direction={"row"}
        bgcolor={"white"}
        borderRadius={2}
        alignItems={"center"}
        boxShadow={"4px 4px 20px rgba(23,33,122,0.3)"}
        px={2}
        sx={{ transform: "translateX(-50%)" }}
      >
        <Box
          fontSize={matches ? 25 : 20}
          width={matches ? 25 : 20}
          height={matches ? 25 : 20}
          color={grey[600]}
        >
          <FiSearch />
        </Box>
        <MainStyledInput
          placeholder="Search Company or CEO"
          value={value ? value : ""}
          onChange={handleChangeSearchValue}
        />
        <Button type="submit" variant="contained">
          Search
        </Button>
      </Stack>
    </Box>
  );
}
