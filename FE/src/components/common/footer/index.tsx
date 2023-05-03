"use client";

import { Box, Stack, Typography } from "@mui/material";
import { deepPurple, grey } from "@mui/material/colors";

export default function Footer() {
  return (
    <Box width={1} borderTop={1} borderColor={deepPurple[100]}>
      <Stack
        direction={"column"}
        width={"calc(100% - 32px)"}
        alignItems={"center"}
        py={4}
        gap={2}
        mx={"auto"}
      >
        <Typography
          variant="h3"
          color={deepPurple[900]}
          fontSize={14}
          fontWeight={700}
        >
          Sentinel Korea Co., Ltd.
        </Typography>
        <Typography fontSize={12} textAlign={"center"}>
          Representative: Jeong Tae-jin | Business Registration Number:
          220-88-25224 <br /> Mail Order Sales Business Report: 2018-Seoul
          Yeongdeungpo-1851 <br />
          Tel: 82-2-2183-0640 | Mobile: 82-10-3252-0420 | E-mail:
          inquiry@sentinelkorea.com <br />
          Address: Daewon Building New Building No. 103 (04328), 49,
          Thickbawi-ro 60-gil, Yongsan-gu
        </Typography>
      </Stack>
      <Box bgcolor={deepPurple[50]} textAlign={"center"} py={2} px={2}>
        <Typography
          variant="h2"
          component={"p"}
          fontSize={10}
          color={grey[600]}
          fontWeight={700}
        >
          SeoulCOPYRIGHT © 2011 SENTINELKOREA Co., Ltd All Rights Reserved.
        </Typography>
      </Box>
    </Box>
  );
}
