"use client";

import { CssBaseline, ThemeProvider } from "@/components/@mui/material";
import { useEffect, useState } from "react";
import { NextAppDirEmotionCacheProvider } from "tss-react/next/appDir";
import { SnackbarProvider } from "notistack";

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
        <SnackbarProvider maxSnack={3}>
          <ThemeProvider theme={theme}>{children}</ThemeProvider>
        </SnackbarProvider>
      </NextAppDirEmotionCacheProvider>
    </>
  );
}
