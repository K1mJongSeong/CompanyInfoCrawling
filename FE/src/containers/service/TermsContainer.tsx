"use client";

import { Tabs, Tab, Box, Typography } from "@mui/material";
import { useState } from "react";

interface TabPanelProps {
  children?: React.ReactNode;
  index: number;
  value: number;
}

function TabPanel(props: TabPanelProps) {
  const { children, value, index, ...other } = props;

  return (
    <div
      role="tabpanel"
      hidden={value !== index}
      id={`simple-tabpanel-${index}`}
      aria-labelledby={`simple-tab-${index}`}
      {...other}
    >
      {value === index && (
        <Box sx={{ p: 3 }}>
          <Typography>{children}</Typography>
        </Box>
      )}
    </div>
  );
}

function a11yProps(index: number) {
  return {
    id: `full-width-tab-${index}`,
    "aria-controls": `full-width-tabpanel-${index}`,
  };
}

export default function TermsContainer() {
  const [value, setValue] = useState(0);

  const handleChange = (event: React.SyntheticEvent, newValue: number) => {
    setValue(newValue);
  };

  return (
    <div
      className="w-screen relative flex items-center justify-center py-10 bg-fixed  min-h-[900px]"
      style={{
        backgroundImage: "url('/assets/images/terms_bg.png",
        backgroundPosition: "center",
      }}
    >
      <div className="w-[calc(100%-32px)] max-w-2xl bg-white rounded-lg max-h-[calc(100%-100px)] py-7 px-4 lg:py-14 lf:px-10 flex flex-col gap-1 items-center">
        <div className="text-lg font-bold">TERMS & Conditions</div>
        <Tabs
          value={value}
          onChange={handleChange}
          textColor="inherit"
          variant="fullWidth"
          aria-label="full width tabs example"
          sx={{ width: 1, px: 3 }}
        >
          <Tab label="Terms to Use" {...a11yProps(0)} />
          <Tab label="Privacy Policy" {...a11yProps(1)} />
        </Tabs>
        <div className="w-full max-h-[650px] overflow-y-auto text-sm text-gray-900">
          <TabPanel value={value} index={0}>
            <iframe
              className="w-full min-h-[500px]"
              src="/assets/terms/terms_english.html"
              frameBorder={0}
            ></iframe>
          </TabPanel>
          <TabPanel value={value} index={1}>
            <iframe
              className="w-full min-h-[500px]"
              src="/assets/terms/policy_english.html"
              frameBorder={0}
            ></iframe>
          </TabPanel>
        </div>
      </div>
    </div>
  );
}
