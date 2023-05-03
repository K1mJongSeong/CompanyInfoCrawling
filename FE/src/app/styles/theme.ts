"use client";
import { createTheme } from "@mui/material/styles";

// Create a theme instance.
const theme = createTheme({
  palette: {
    mode: "light",
  },
  typography: {
    fontFamily: ["__pretendard_d46352", "__pretendard_Fallback_d46352"].join(
      ","
    ),
  },
});

export default theme;
