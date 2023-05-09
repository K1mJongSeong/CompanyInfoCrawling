"use client";
import Img from "@/components/common/Image";
import { MainSearchBox, MainStyledInput } from "@/components/main/styled";
import {
  useMediaQuery,
  Stack,
  Typography,
  Box,
  Button,
  useTheme,
} from "@mui/material";
import { grey } from "@mui/material/colors";
import { FiSearch } from "react-icons/fi";
import { useState } from "react";
import { useRouter } from "next/navigation";
import { useSnackbar } from "notistack";
import { GotoSearch } from "@/service/search_service";

export default function HomeContainer() {
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

  return (
    <Stack
      direction={"column"}
      width={1}
      height={1}
      minHeight={600}
      position={"relative"}
      justifyContent={"flex-end"}
      mb={10}
    >
      <MainSearchBox position={"absolute"} top={"50%"} left={"50%"} zIndex={8}>
        <Stack direction={"column"} alignItems={"center"} gap={matches ? 1 : 2}>
          <Typography
            variant="h2"
            component={"h3"}
            fontSize={28}
            fontWeight={700}
          >
            Search for the company information you want
          </Typography>
          <Typography
            variant="subtitle1"
            component={"p"}
            color={grey[500]}
            fontSize={matches ? 16 : 12}
          >
            Lorem Ipsum is simply dummy text of the printing and typesetting
            industry.
          </Typography>
        </Stack>
        <Stack
          component="form"
          onSubmit={handleSubmit}
          width={1}
          height={70}
          direction={"row"}
          bgcolor={"white"}
          borderRadius={2}
          alignItems={"center"}
          boxShadow={"4px 4px 20px rgba(23,33,122,0.3)"}
          px={2}
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
      </MainSearchBox>
      <Img src={"/assets/images/main_bg.png"} alt="main background" />
    </Stack>
  );
}
