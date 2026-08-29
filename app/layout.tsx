import type { ReactNode } from 'react';

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="ar" dir="rtl">
      <head>
        <meta charSet="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <title>MVTeaches Owner Demo</title>
      </head>
      <body style={{ margin: 0 }}>{children}</body>
    </html>
  );
}
