=head1 NAME

PPIx::Regexp::Token::Backtrack - Represent backtrack control.

=head1 SYNOPSIS

 use PPIx::Regexp::Dumper;
 PPIx::Regexp::Dumper->new( 'qr{(*ACCEPT)}smx' )
     ->print();

=head1 INHERITANCE

C<PPIx::Regexp::Token::Backtrack> is a
L<PPIx::Regexp::Token|PPIx::Regexp::Token>.

C<PPIx::Regexp::Token::Backtrack> has no descendants.

=head1 DESCRIPTION

This class represents one of the backtrack controls.

=head1 METHODS

This class provides no public methods beyond those provided by its
superclass.

=cut

package PPIx::Regexp::Token::Backtrack;

use strict;
use warnings;

use base qw{ PPIx::Regexp::Token };

our $VERSION = '0.028';

# Return true if the token can be quantified, and false otherwise
sub can_be_quantified { return };

sub perl_version_introduced {
    return '5.009005';
}

# This must be implemented by tokens which do not recognize themselves.
# The return is a list of list references. Each list reference must
# contain a regular expression that recognizes the token, and optionally
# a reference to a hash to pass to make_token as the class-specific
# arguments. The regular expression MUST be anchored to the beginning of
# the string.
sub __PPIX_TOKEN__recognize {
    return ( [ qr{ \A \( \* [^\)]* \) }smx ] );
}

# This class gets recognized by PPIx::Regexp::Token::Structure as part
# of its left parenthesis processing.

=begin comment

sub __PPIX_TOKENIZER__regexp {
    my ( $class, $tokenizer, $character ) = @_;

    return $character eq 'x' ? 1 : 0;
}

=end comment

=cut

1;

__END__

=head1 SUPPORT

Support is by the author. Please file bug reports at
L<http://rt.cpan.org>, or in electronic mail to the author.

=head1 AUTHOR

Thomas R. Wyant, III F<wyant at cpan dot org>

=head1 COPYRIGHT AND LICENSE

Copyright (C) 2009-2012 by Thomas R. Wyant, III

This program is free software; you can redistribute it and/or modify it
under the same terms as Perl 5.10.0. For more details, see the full text
of the licenses in the directory LICENSES.

This program is distributed in the hope that it will be useful, but
without any warranty; without even the implied warranty of
merchantability or fitness for a particular purpose.

=cut

# ex: set textwidth=72 :
