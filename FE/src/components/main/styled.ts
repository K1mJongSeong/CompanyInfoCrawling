import { media } from "@/app/styles/theme";
import styled from "@emotion/styled";
import { Box } from "@mui/material";

export const MainSearchBox = styled(Box)`
  width: calc(100% - 32px);
  max-width: 800px;
  position: absolute;
  height: max-content;
  top: 120px;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 60px;
`;

export const MainStyledInput = styled.input`
  flex: 1;
  padding: 0 20px;
  border: none;
  font-size: 1.125rem;
  background: none;
  &:focus {
    outline: none;
  }

  ${media.tablet} {
    padding: 0 8px;
    width: 100%;
    font-size: 1rem;
  }
`;
