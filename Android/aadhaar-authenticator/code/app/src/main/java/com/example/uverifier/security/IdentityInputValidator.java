package com.example.uverifier.security;

import java.util.regex.Pattern;

/** Validation helpers for identity workflow inputs. Never logs or persists raw identifiers. */
public final class IdentityInputValidator {
    private static final Pattern DIGITS_12 = Pattern.compile("^\\d{12}$");
    private static final Pattern OTP_6 = Pattern.compile("^\\d{6}$");
    private static final Pattern MOBILE_10 = Pattern.compile("^[6-9]\\d{9}$");

    private static final int[][] D = {
            {0,1,2,3,4,5,6,7,8,9},{1,2,3,4,0,6,7,8,9,5},
            {2,3,4,0,1,7,8,9,5,6},{3,4,0,1,2,8,9,5,6,7},
            {4,0,1,2,3,9,5,6,7,8},{5,9,8,7,6,0,4,3,2,1},
            {6,5,9,8,7,1,0,4,3,2},{7,6,5,9,8,2,1,0,4,3},
            {8,7,6,5,9,3,2,1,0,4},{9,8,7,6,5,4,3,2,1,0}
    };
    private static final int[][] P = {
            {0,1,2,3,4,5,6,7,8,9},{1,5,7,6,2,8,3,0,9,4},
            {5,8,0,3,7,9,6,1,4,2},{8,9,1,6,0,4,3,5,2,7},
            {9,4,5,3,1,2,6,8,7,0},{4,2,8,6,5,7,3,9,0,1},
            {2,7,9,3,8,0,6,4,1,5},{7,0,4,6,9,1,3,2,5,8}
    };

    private IdentityInputValidator() { }

    public static boolean isValidAadhaar(String value) {
        if (value == null || !DIGITS_12.matcher(value).matches()) return false;
        int checksum = 0;
        int position = 0;
        for (int i = value.length() - 1; i >= 0; i--, position++) {
            int digit = value.charAt(i) - '0';
            checksum = D[checksum][P[position % 8][digit]];
        }
        return checksum == 0;
    }

    public static boolean isValidOtp(String value) {
        return value != null && OTP_6.matcher(value).matches();
    }

    public static boolean isValidIndianMobile(String value) {
        return value != null && MOBILE_10.matcher(value).matches();
    }

    public static String maskAadhaar(String value) {
        if (value == null || value.length() != 12) return "••••••••••••";
        return "••••••••" + value.substring(8);
    }

    public static String maskMobile(String value) {
        if (value == null || value.length() != 10) return "••••••••••";
        return "••••••" + value.substring(6);
    }
}
