"use client";

import { CssBaseline, ThemeProvider } from "@mui/material";
import { useEffect, useState } from "react";
import { NextAppDirEmotionCacheProvider } from "tss-react/next/appDir";

import theme from "./styles/theme";
import DefaultLoading from "./loading";

type Props = {
  children: React.ReactNode;
};

export default function MuiSetup({ children }: Props) {
  const [mounted, setMounted] = useState<boolean>(false);

  useEffect(() => {
    setMounted(true);
  }, []);
  if (!mounted) return <DefaultLoading />;
  return (
    <>
      <CssBaseline />
      <NextAppDirEmotionCacheProvider options={{ key: "css" }}>
        <ThemeProvider theme={theme}>{children}</ThemeProvider>
      </NextAppDirEmotionCacheProvider>
    </>
  );
}
