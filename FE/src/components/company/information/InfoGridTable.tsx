import { Stack, Typography, useMediaQuery, useTheme } from "@mui/material";
import { grey } from "@mui/material/colors";
import uuid from "react-uuid";

export default function InfoGridTable() {
  return (
    <div className="grid w-full grid-cols-1 gap-x-8 gap-y-2 sm:grid-cols-2 md:grid-cols-3">
      {Array.from(Array(4)).map((_) => (
        <IngoGridItem key={uuid()} />
      ))}
    </div>
  );
}

export const IngoGridItem = () => {
  const theme = useTheme();
  const matches = useMediaQuery(theme.breakpoints.up("md"));
  return (
    <Stack
      direction={"row"}
      borderBottom={1}
      borderColor={grey[300]}
      height={40}
      alignItems={"center"}
      justifyContent={"space-between"}
      px={matches ? 2 : 1}
    >
      <Typography fontSize={"12px"} color={grey[500]}>
        Company Info
      </Typography>
      <Typography fontSize={"12px"} fontWeight={500}>
        example
      </Typography>
    </Stack>
  );
};
