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
    fontFamily: "Pretendard",
  },
  breakpoints: {
    values: {
      xs: 0,
      sm: 600,
      md: 900,
      lg: 1200,
      xl: 1536,
    },
  },
});

const customMediaQuery = (maxWidth: number): string =>
  `@media (max-width: ${maxWidth}px)`;

export const media = {
  custom: customMediaQuery,
  pc: customMediaQuery(1440),
  tablet: customMediaQuery(1024),
  mobile: customMediaQuery(768),
};

export default theme;
