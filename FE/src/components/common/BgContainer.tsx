"use client";

import { Box } from "@mui/material";
import styled from "@emotion/styled";

export default function BgContainer({
  children,
}: {
  children: React.ReactNode;
}) {
  return <BgBlock>{children}</BgBlock>;
}

const BgBlock = styled(Box)`
  width: 100%;
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
`;
