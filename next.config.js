/** @type {import('next').NextConfig} */
const nextConfig = {
  output: "export",
  // Re-writes dont work with Tauri...since output above is set to "export"
  // rewrites: async () => {
  //   return [
  //     {
  //       source: "/api/v1/text/:path*",
  //       destination:
  //         process.env.NODE_ENV === "development"
  //           ? "http://127.0.0.1:8008/api/v1/text/:path*"
  //           : "/api/v1/text/:path*",
  //     },
  //   ];
  // },
};

module.exports = nextConfig;
