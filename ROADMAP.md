# Roadmap

Andarun is built in versions, and each version in phases. A phase is finished when its exit criteria are met, including tests. Dates are added only once a phase is committed to.

Progress is also tracked with GitHub milestones, one per version.

## v1: text-only social network

**Goal:** a small, invite-only community can sign up, write and discuss text posts, and keep using the site on a domestic network with no outside services.

### Phase 1.1: accounts (in progress)

- [x] Project setup with settings read from the environment; `SECRET_KEY` required, `DEBUG` off by default
- [x] Custom user model with username login; usernames limited to `[a-z0-9_]{3,20}` and stored in lowercase
- [x] Admin for the custom user model
- [ ] Login, logout and password change
- [ ] Tests for the user model, the manager and the admin forms

Exit criteria: a member can log in and out and change their password; all of the above is covered by tests.

### Phase 1.2: invitations

- [ ] Invite codes generated with `secrets`, using a readable alphabet without look-alike characters
- [ ] Per-member invite quota, checked under a row lock inside a transaction so that concurrent requests cannot exceed it
- [ ] Retry on code collisions inside a nested savepoint, so a unique-constraint error does not break the outer transaction
- [ ] Sign-up with an invite code; the new account stays pending until the member who invited it approves it
- [ ] Invitation tree: every account records who invited it

Exit criteria: sign-up works only with a valid code; quotas hold under concurrent requests; tests cover reused codes, over-quota requests and pending approvals.

### Phase 1.3: profiles and posts

- [ ] Profile page with university and field of study
- [ ] Text posts: create, edit, delete
- [ ] Comments and likes
- [ ] Public and private profiles

### Phase 1.4: social graph and feed

- [ ] Follow and unfollow
- [ ] Home feed of followed members, paginated
- [ ] Saved posts

### Phase 1.5: discovery and notifications

- [ ] Search for members and posts
- [ ] Notifications for follows, comments and likes

### Phase 1.6: release

- [ ] PostgreSQL in production
- [ ] Docker image and Compose file
- [ ] `python manage.py check --deploy` passes
- [ ] Continuous integration: tests and checks on every push
- [ ] `v1.0.0` tag and changelog

## v2: messaging (planned)

- Direct messages between members
- Group conversations
- End-to-end encryption for messages, so the server stores only ciphertext

## v3: mobile and real time (planned)

- Separate mobile clients for iOS and Android
- Real-time updates with Django Channels

## v4: media (planned)

- Image posts and profile photos
- Object storage for uploaded files
