"use client";
import { Button, Stack, Typography } from "@mui/material";
import Img from "../common/Image";
import { NoSearchBgBlock } from "./styles";
import { grey, indigo } from "@mui/material/colors";
import { useRouter } from "next/navigation";

export default function NoSearch() {
  const router = useRouter();
  return (
    <NoSearchBgBlock>
      <Stack
        direction={"column"}
        width={"calc(100% - 32px)"}
        alignItems={"center"}
        maxWidth={300}
      >
        <Img
          src={"/assets/images/nosearch.svg"}
          alt="no search result"
          style={{ marginBottom: "1rem", maxWidth: "128px" }}
        />
        <Typography
          variant="h2"
          fontSize={20}
          mb={1}
          color={indigo[500]}
          fontWeight={"bold"}
        >
          Empty
        </Typography>
        <Typography variant="body1" fontSize={14} mb={5} color={grey[500]}>
          {"There's no search result"}
        </Typography>
        <Button variant="contained" fullWidth onClick={() => router.push("/")}>
          HOME
        </Button>
      </Stack>
    </NoSearchBgBlock>
  );
}
