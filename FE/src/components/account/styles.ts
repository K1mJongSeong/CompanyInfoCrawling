import { media } from "@/app/styles/theme";
import styled from "@emotion/styled";
import { Box, Container, Stack } from "@mui/material";

export const AcountContainer = styled(Container)`
  padding: 80px 1rem;
  height: max-content;
  min-height: 800px;
  display: flex;
  align-items: center;
  justify-content: center;
  ${media.tablet} {
    padding: 2rem 1rem 80px;
    min-height: auto;
  }
`;

export const AcountCard = styled(Box)`
  width: 100%;
  border-radius: 10px;
  background-color: white;
  box-shadow: 4px 4px 20px rgba(23, 33, 122, 0.3);
  padding: 30px 1.5rem;
`;
