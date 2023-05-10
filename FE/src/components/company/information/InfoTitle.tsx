"use client";

import { Box, Typography, useMediaQuery, useTheme } from "@mui/material";

export default function InfoTitle({ title }: { title: string }) {
  const theme = useTheme();
  const matches = useMediaQuery(theme.breakpoints.up("md"));
  return (
    <Box
      py={2}
      px={matches ? 2 : 1}
      mb={2}
      borderBottom={1}
      borderColor={"#5B7FFF"}
    >
      <Typography variant="h2" fontWeight={"bold"} fontSize={"1rem"}>
        {title}
      </Typography>
    </Box>
  );
}
