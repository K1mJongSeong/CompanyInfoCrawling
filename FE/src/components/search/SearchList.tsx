"use client";

import { Divider, Stack, Typography } from "@mui/material";
import { grey } from "@mui/material/colors";
import Link from "next/link";

export default function SearchList({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <Stack direction={"column"} gap={2} mb={5}>
      {children}
    </Stack>
  );
}
export const SearchItem = () => {
  return (
    <Link href="/">
      <Stack
        direction={"column"}
        gap={1}
        width={1}
        py={3}
        px={2}
        bgcolor={grey[100]}
        border={"1px solid"}
        borderColor={grey[400]}
        borderRadius={2}
      >
        <Stack direction={"row"}>
          <Typography variant="h3" fontSize={"large"} fontWeight={"bold"}>
            COMPANY NAME
          </Typography>
        </Stack>
        <Stack
          direction={"row"}
          gap={3}
          divider={<Divider orientation="vertical" flexItem />}
        >
          <Typography variant="body1" fontSize={"14px"}>
            CEO NAME
          </Typography>
          <Typography variant="body1" fontSize={"14px"}>
            BUSINESS NUMBER
          </Typography>
          <Typography variant="body1" fontSize={"14px"}>
            CORPARATE FROM
          </Typography>
        </Stack>
        <Stack direction={"row"}>
          <Typography variant="body2" fontSize={"small"} color={grey[500]}>
            Establishment
          </Typography>
        </Stack>
      </Stack>
    </Link>
  );
};
