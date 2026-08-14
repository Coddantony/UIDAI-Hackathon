package com.example.uverifier.security;

import java.util.regex.Pattern;

/** Validation helpers for identity workflow inputs. Never logs or persists raw identifiers. */
public final class IdentityInputValidator {
    private static final Pattern DIGITS_12 = Pattern.compile("^\\d{12}$");
    private static final Pattern OTP_6 = Pattern.compile("^\\d{6}$");
    private static final Pattern MOBILE_10 = Pattern.compile("^[6-9]\\d{9}$");

    private IdentityInputValidator() { }

    public static boolean isValidAadhaar(String value) {
        if (value == null || !DIGITS_12.matcher(value).matches()) return false;
        int sum = 0;
        for (int i = 0; i < 12; i++) {
            int digit = value.charAt(i) - '0';
            sum += (i % 2 == 0) ? digit : (digit * 3);
        }
        return sum % 10 == 0;
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
