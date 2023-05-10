"use client";

import CampanyProfile from "@/components/company/common/CampanyProfile";
import InfoGridTable from "@/components/company/information/InfoGridTable";
import InfoReport from "@/components/company/information/InfoReport";
import InfoTitle from "@/components/company/information/InfoTitle";
import { Box, Stack } from "@mui/material";

export default function CompanyInfoContainer() {
  return (
    <>
      <CampanyProfile pdf />
      <Stack direction={"column"} gap={3}>
        <Box>
          <InfoTitle title="Company Overview" />
          <InfoGridTable />
        </Box>
        <Box>
          <InfoTitle title="Management" />
          <InfoGridTable />
        </Box>
        <Box>
          <InfoTitle title="Stockholder" />
          <InfoGridTable />
        </Box>
        <Box>
          <InfoTitle title="Report Articles" />
          <InfoReport />
        </Box>
      </Stack>
    </>
  );
}
