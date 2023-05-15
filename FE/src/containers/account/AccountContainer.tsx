"use client";
import { AcountContainer, AcountCard } from "@/components/account/styles";
import { Stack, Typography } from "@mui/material";
import { blue } from "@mui/material/colors";

export default function AccountContainer({ id }: { id: string }) {
  return (
    <AcountContainer>
      <AcountCard maxWidth={590}>
        <Stack direction={"column"}>
          <Typography variant="h2" fontSize={18} fontWeight={"bold"} mb={5}>
            MYPAGE
            <Typography fontSize={12} color={blue[500]} ml={1}>
              (Individual)
            </Typography>
          </Typography>
          {id}
        </Stack>
      </AcountCard>
    </AcountContainer>
  );
}
