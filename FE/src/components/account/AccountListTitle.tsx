"use client";

import { Link, Stack, Typography } from "@mui/material";
import { blue, grey } from "@mui/material/colors";
import Image from "next/image";

export default function AccountListTitle({
  title,
  goto,
}: {
  title: string;
  goto: string;
}) {
  return (
    <Stack
      direction={"row"}
      justifyContent={"space-between"}
      alignItems={"center"}
      py={1}
      mb={0.5}
    >
      <Typography fontSize={12} color={grey[500]}>
        {title}
      </Typography>
      <Link
        href={goto}
        color={"#5B7FFF"}
        fontSize={12}
        underline="always"
        display={"flex"}
        alignItems={"center"}
      >
        more
        <Image
          src={"/assets/images/arrow_right.png"}
          alt="arrow"
          style={{ marginLeft: "4px" }}
        />
      </Link>
    </Stack>
  );
}
