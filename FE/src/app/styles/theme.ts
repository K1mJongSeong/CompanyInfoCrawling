"use client";
import { createTheme } from "@mui/material/styles";

declare module "@mui/material" {
  interface ButtonPropsColorOverrides {
    rg: true;
  }
}
// Create a theme instance.
const theme = createTheme({
  palette: {
    mode: "light",
    primary: {
      main: "#17217A",
    },
  },
  typography: {
    fontFamily: ["__pretendard_d46352", "__pretendard_Fallback_d46352"].join(
      ","
    ),
  },
});

export default theme;
