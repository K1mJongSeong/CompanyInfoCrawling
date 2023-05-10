"use client";

import { media } from "@/app/styles/theme";
import styled from "@emotion/styled";
import { Box } from "@mui/material";
import { CompanyCard, CompanyLayoutContainer, CompanyTopBgBox } from "./styles";

export default function CaompanyLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <BgBlock>
      <CompanyLayoutContainer>
        <CompanyTopBgBox />
        <CompanyCard>{children}</CompanyCard>
      </CompanyLayoutContainer>
    </BgBlock>
  );
}

const BgBlock = styled(Box)`
  width: 100vw;
  height: max-content;
  min-height: 820px;
  background: #f1f4ff; /* Old browsers */
  background: -moz-linear-gradient(
    -45deg,
    #f1f4ff 0%,
    #f8f8f8 100%,
    #7db9e8 100%
  ); /* FF3.6-15 */
  background: -webkit-linear-gradient(
    -45deg,
    #f1f4ff 0%,
    #f8f8f8 100%,
    #7db9e8 100%
  ); /* Chrome10-25,Safari5.1-6 */
  background: linear-gradient(
    135deg,
    #f1f4ff 0%,
    #f8f8f8 100%,
    #7db9e8 100%
  ); /* W3C, IE10+, FF16+, Chrome26+, Opera12+, Safari7+ */
  filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#f1f4ff', endColorstr='#7db9e8',GradientType=1 ); /* IE6-9 fallback on horizontal gradient */
  ${media.tablet} {
    min-height: auto;
  }
`;
