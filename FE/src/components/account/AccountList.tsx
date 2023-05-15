"use client";

import { Stack, Typography } from "@mui/material";
import { grey, indigo } from "@mui/material/colors";

export default function AccountList({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <Stack direction={"column"} mb={5}>
      {children}
    </Stack>
  );
}

export const AccountListHead = ({
  children,
}: {
  children: React.ReactNode;
}) => {
  return (
    <Stack
      direction={"row"}
      alignItems={"center"}
      height={40}
      borderBottom={1}
      borderColor={indigo[500]}
      color={indigo[700]}
    >
      {children}
    </Stack>
  );
};

export const AccountListRow = ({ children }: { children: React.ReactNode }) => {
  return (
    <Stack
      direction={"row"}
      alignItems={"center"}
      height={54}
      borderBottom={1}
      borderColor={grey[400]}
    >
      {children}
    </Stack>
  );
};
export const AccountTd = ({ children }: { children: React.ReactNode }) => {
  return (
    <Stack
      width={1}
      overflow={"hidden"}
      textOverflow={"ellipsis"}
      whiteSpace={"nowrap"}
      px={1}
    >
      <Typography fontSize={12}>{children}</Typography>
    </Stack>
  );
};
