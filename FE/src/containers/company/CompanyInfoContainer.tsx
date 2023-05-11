"use client";

import CampanyProfile from "@/components/company/common/CampanyProfile";
import InfoGridTable from "@/components/company/information/InfoGridTable";
import InfoReport from "@/components/company/information/InfoReport";
import InfoTitle from "@/components/company/information/InfoTitle";
import ReportModal from "@/components/company/information/report/ReportModal";
import { Box, Stack } from "@mui/material";
import { useState } from "react";

export default function CompanyInfoContainer() {
  const [open, setOpen] = useState(false);

  const handleClickOpen = () => {
    setOpen(true);
  };

  const handleClose = () => {
    setOpen(false);
  };
  return (
    <>
      <CampanyProfile pdf onClickOpenPdf={handleClickOpen} />
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
      <ReportModal open={open} close={handleClose} />
    </>
  );
}
