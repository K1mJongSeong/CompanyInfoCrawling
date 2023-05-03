import { Metadata } from "next/dist/lib/metadata/types/metadata-interface";
import MuiSetup from "./MuiSetup";
import "./styles/globals.css";
import localFont from "next/font/local";
import Header from "@/components/common/header";
import Footer from "@/components/common/footer";

const pretendard = localFont({
  src: [
    {
      path: "./styles/fonts/pretendard/Pretendard-Light.woff2",
      weight: "300",
      style: "normal",
    },
    {
      path: "./styles/fonts/pretendard/Pretendard-Regular.woff2",
      weight: "400",
      style: "normal",
    },
    {
      path: "./styles/fonts/pretendard/Pretendard-Medium.woff2",
      weight: "500",
      style: "normal",
    },
    {
      path: "./styles/fonts/pretendard/Pretendard-Bold.woff2",
      weight: "700",
      style: "normal",
    },
  ],
});

export const metadata: Metadata = {
  title: "Sentinel Korea KYC",
  description: "Enterprise Information Delivery Platform | Sentinel Korea KYC",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className={pretendard.className}>
        <MuiSetup>
          <Header />
          {children}
          <Footer />
        </MuiSetup>
      </body>
    </html>
  );
}
