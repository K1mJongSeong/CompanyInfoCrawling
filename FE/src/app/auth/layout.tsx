import AuthLayoutBlock from "@/components/common/AuthLayoutBlock";
import BgContainer from "@/components/common/BgContainer";
import { Metadata } from "next/types";

export const metadata: Metadata = {
  title: "Auth | Sentinel Korea KYC",
  description: "Enterprise Information Delivery Platform | Sentinel Korea KYC",
};

export default function AuthLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <AuthLayoutBlock>
      <BgContainer>{children}</BgContainer>
    </AuthLayoutBlock>
  );
}
