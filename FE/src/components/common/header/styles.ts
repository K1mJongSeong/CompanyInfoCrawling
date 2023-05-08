import styled from "@emotion/styled";
import { Box, Button, Input, Typography, css } from "@mui/material";
import Link from "next/link";

interface LinkProps {
  isActive: boolean;
}

export const StyledLink = styled(Link)<LinkProps>`
  &:hover {
    color: #17217a;
  }

  ${(props) =>
    props.isActive &&
    css`
      color: #17217a;
    `}
`;

export const StyledButton = styled(Button)`
  background-color: #f1f4ff;
  width: 30px;
  min-width: auto;
  padding: 0;
  height: 30px;
  font-size: 1.125rem;
`;

export const Spacer = styled(Box)`
  width: 100%;
  height: 60px;
`;

export const SearchCloseBtn = styled(Button)`
  background-color: white;
  border: none;
  padding: 4px 8px;
  &:hover {
    opacity: 0.8;
  }
`;

export const SearchInput = styled(Input)`
  ::before {
    border-color: #beb0ff6b;
  }
`;
