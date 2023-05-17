import { media } from "@/app/styles/theme";
import styled from "@emotion/styled";
import { LoadingButton } from "@mui/lab";
import { Box, Checkbox, Container, Tab, Tabs } from "@mui/material";
import { grey, indigo } from "@mui/material/colors";

export const AuthContainer = styled(Container)`
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

export const AuthCard = styled(Box)`
  width: 100%;
  border-radius: 10px;
  background-color: white;
  box-shadow: 4px 4px 20px rgba(23, 33, 122, 0.3);
  padding: 50px 1.5rem;
`;
export const AuthLoginBtn = styled(LoadingButton)`
  width: 100%;
  max-width: 192px;
  margin-top: 32px;
`;

export const RegisterTabs = styled(Tabs)`
  min-height: 33px;
  span.css-yowank-MuiTabs-indicator {
    background-color: ${indigo[300]};
  }
`;

export const RegisterTab = styled(Tab)`
  width: 50%;
  min-height: auto;
  height: 33px;
  color: ${grey[500]};

  &.Mui-selected {
    color: ${indigo[300]};
  }
`;

export const AuthCheckBox = styled(Checkbox)`
  width: 24px;
  height: 24px;
  padding: 2px;
  margin-right: 5px;
`;
